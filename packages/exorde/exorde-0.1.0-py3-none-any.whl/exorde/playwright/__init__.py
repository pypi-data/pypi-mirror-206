"""
It uses playwright as a browser interface

developement note on pages:

Pages were initially initialized as lists. However even if lists have an
element identifier and can be accessed trough an index (l[index]) ;
identifying and updating a single element is a chore, this is because our
find function which is used in oversight etc... doesn't integrate these.
"""
from pathlib import Path
import random, os, json
import logging

from playwright_stealth import stealth_async
from playwright.async_api import async_playwright
from aiosow.routines import routine
from aiosow.bindings import perpetuate, autofill
from typing import Callable
import subprocess


async def setup_playwright(
    user_agent, no_headless, playwright, browser, context, pages
):
    """Initialize Playwright and install it if required"""
    logging.debug("setup playwright")
    cookies = None
    cookiefile = os.path.join(
        Path(os.path.expanduser("~")).resolve(), ".config", "exorde", "cookies.json"
    )
    if playwright:
        for page in pages:
            await pages[page]["page"].close()
        cookies = await context.cookies()
        with open(cookiefile, "w") as f:
            json.dump(cookies, f)

        await context.close()
        await browser.close()
        await playwright.stop()
    pwright = await async_playwright().start()
    subprocess.run(["playwright", "install", "chromium"])
    browser = await pwright.chromium.launch(headless=not no_headless)
    context = await browser.new_context(user_agent=user_agent)
    if not cookies:
        try:
            with open(cookiefile, "r") as f:
                cookies = json.load(f)
        except:
            pass
    if cookies:
        await context.add_cookies(cookies)
    return {
        "playwright": pwright,
        "browser": browser,
        "context": context,
    }


response_hooks = {}


def response(filter: Callable):
    """
    Calls the decorated function whenever playwright has intercepted a response
    which URL matches the one provided.
    """

    def wrapper(function: Callable):
        if not response_hooks.get(filter):
            response_hooks[filter] = [function]
        else:
            response_hooks[filter].append(function)
        return function

    return wrapper


def response_hook(memory: dict) -> Callable:
    async def hook(response):
        """Called by playwright on every new response"""
        nonlocal memory
        try:
            for _hook, funcs in response_hooks.items():
                if _hook(response):
                    logging.debug("intercepted %s...", response.url[:140])
                    for func in funcs:
                        try:
                            content = await response.json()
                        except:
                            content = response
                        await autofill(func, args=(content,), memory=memory)
        except Exception as error:
            logging.error("Error treating hooked response", error)
            raise (error)

    return hook


async def create_page(page_id, context, memory):  # every page share the same context
    """Create a page to be managed"""
    logging.debug("creates page %d", page_id)
    page = await context.new_page()
    page.on("response", response_hook(memory))
    await stealth_async(page)
    return page


PAGE_ACTIONS = []


def on_available_browser_tab(function):
    logging.debug("%s registered on available_browser tab", function)
    PAGE_ACTIONS.append(function)
    return function


async def manage_page(page, tab_lifetime, memory):
    """Launch a scraping method, sets page as taken and conjure availability"""
    page_id, page_descr = page

    def roll_page():
        """Rolls and update on page and specifies it as available"""
        nonlocal page_id, page_descr
        logging.debug("Rolling page %s as available", page)
        return {"pages": {page_id: {"page": page_descr["page"], "available": True}}}

    if len(PAGE_ACTIONS) > 1:
        action = random.choice(PAGE_ACTIONS)
    elif len(PAGE_ACTIONS) == 1:
        action = PAGE_ACTIONS[0]
    else:
        action = None
    if action:
        await perpetuate(action, args=(page,), memory=memory)
    routine(frequency=-int(tab_lifetime))(roll_page)
