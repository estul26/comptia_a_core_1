const { test, expect } = require("@playwright/test");
const fs = require("fs");
const path = require("path");

async function selectObjective(page, needle) {
  const value = await page.locator("#mobileLessonSelect option").evaluateAll(
    (options, text) => options.find(option => option.textContent.includes(text))?.value || "",
    needle
  );
  expect(value, `Missing objective option containing: ${needle}`).not.toBe("");
  await page.locator("#mobileLessonSelect").selectOption(value);
  await page.waitForTimeout(80);
  return value;
}

async function documentRatio(page) {
  return page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    return max > 0 ? scrollY / max : 0;
  });
}

test.beforeEach(async ({ page }) => {
  await page.addInitScript(() => localStorage.clear());
  await page.goto("/", { waitUntil: "domcontentloaded" });
  await expect(page.locator("#mobileLessonSelect")).toBeVisible();
});

test("mobile layout uses one scroll surface and touch-sized controls", async ({ page }) => {
  const metrics = await page.evaluate(() => {
    const pane = document.querySelector(".pane");
    const bottom = document.querySelector(".bottom");
    const summary = document.querySelector(".more-menu > summary");
    const language = document.querySelector("#languageMode");
    const next = document.querySelector("#nextBtn");
    const rect = element => {
      const r = element.getBoundingClientRect();
      return { width: r.width, height: r.height, top: r.top, bottom: r.bottom };
    };
    return {
      coarse: matchMedia("(pointer:coarse)").matches,
      horizontalOverflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      paneOverflowY: getComputedStyle(pane).overflowY,
      paneScrollDelta: pane.scrollHeight - pane.clientHeight,
      syncDisplay: getComputedStyle(document.querySelector("#syncBtn")).display,
      bottomPosition: getComputedStyle(bottom).position,
      summary: rect(summary),
      language: rect(language),
      next: rect(next)
    };
  });

  expect(metrics.coarse).toBe(true);
  expect(metrics.horizontalOverflow).toBeLessThanOrEqual(1);
  expect(metrics.paneOverflowY).toBe("visible");
  expect(Math.abs(metrics.paneScrollDelta)).toBeLessThanOrEqual(2);
  expect(metrics.syncDisplay).toBe("none");
  expect(metrics.bottomPosition).toBe("fixed");
  expect(metrics.summary.height).toBeGreaterThanOrEqual(44);
  expect(metrics.language.height).toBeGreaterThanOrEqual(44);
  expect(metrics.next.height).toBeGreaterThanOrEqual(44);
  await expect(page.locator("#mobileProgress")).toHaveText("0 / 27 complete · 0%");
});

test("language modes and objective navigation remain usable", async ({ page }) => {
  const language = page.locator("#languageMode");

  await language.selectOption("en");
  await expect(page.locator("#enPane")).toBeVisible();
  await expect(page.locator("#ugPane")).toBeHidden();

  await language.selectOption("ug");
  await expect(page.locator("#enPane")).toBeHidden();
  await expect(page.locator("#ugPane")).toBeVisible();

  await language.selectOption("both");
  await expect(page.locator("#enPane")).toBeVisible();
  await expect(page.locator("#ugPane")).toBeVisible();

  const first = await selectObjective(page, "Objective 1.1");
  expect(page.locator("#mobileLessonSelect")).toHaveValue(first);

  await page.locator("#nextBtn").click();
  await expect(page.locator("#mobileLessonSelect")).toHaveValue(String(Number(first) + 1));

  await page.locator("#prevBtn").click();
  await expect(page.locator("#mobileLessonSelect")).toHaveValue(first);
});

test("More menu closes on outside tap and Escape returns focus", async ({ page }) => {
  const details = page.locator("details.more-menu");
  const summary = details.locator("summary");

  await summary.click();
  await expect(details).toHaveAttribute("open", "");
  const popover = await page.locator(".more-popover").boundingBox();
  const viewport = page.viewportSize();
  expect(popover).not.toBeNull();
  expect(viewport).not.toBeNull();
  await page.mouse.click(Math.max(4, popover.x - 12), Math.min(viewport.height - 80, popover.y + 80));
  await expect(details).not.toHaveAttribute("open", "");

  await summary.click();
  await expect(details).toHaveAttribute("open", "");
  await page.keyboard.press("Escape");
  await expect(details).not.toHaveAttribute("open", "");
  await expect(summary).toBeFocused();
});

test("Reading Focus follows the visible paragraph while scrolling", async ({ page }) => {
  await selectObjective(page, "Objective 1.1");

  const details = page.locator("details.more-menu");
  await details.locator("summary").click();
  await page.locator("#focusLineBtn").click();
  await page.keyboard.press("Escape");

  const focused = page.locator(".article .focus-line");
  await expect(focused).toHaveCount(1);
  const before = (await focused.textContent() || "").trim();

  await page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    scrollTo(0, max * 0.55);
  });
  await page.waitForTimeout(200);

  await expect(focused).toHaveCount(1);
  const after = (await focused.textContent() || "").trim();
  expect(after).not.toBe(before);

  const visibility = await focused.evaluate(element => {
    const r = element.getBoundingClientRect();
    const top = document.querySelector(".top")?.getBoundingClientRect().bottom || 0;
    const bottom = document.querySelector(".bottom")?.getBoundingClientRect().top || innerHeight;
    return { elementTop: r.top, elementBottom: r.bottom, visibleTop: top, visibleBottom: bottom };
  });
  expect(visibility.elementBottom).toBeGreaterThan(visibility.visibleTop);
  expect(visibility.elementTop).toBeLessThan(visibility.visibleBottom);
});

test("Resume reading restores the saved mobile document position", async ({ page }) => {
  await selectObjective(page, "Objective 1.1");

  await page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    scrollTo(0, max * 0.4);
  });
  await page.waitForTimeout(220);

  const stored = await page.evaluate(() => Number(localStorage.getItem("a1-scroll-ratio-1.1") || 0));
  expect(stored).toBeGreaterThan(0.2);

  await selectObjective(page, "Objective 1.2");
  await selectObjective(page, "Objective 1.1");
  expect(await documentRatio(page)).toBeLessThan(0.08);

  const details = page.locator("details.more-menu");
  await details.locator("summary").click();
  await expect(page.locator("#resumePill")).toBeVisible();
  await page.locator("#resumePill").click();
  await page.waitForTimeout(120);

  const restored = await documentRatio(page);
  expect(restored).toBeGreaterThan(0.2);
  expect(Math.abs(restored - stored)).toBeLessThan(0.15);
});

test("Cards and Columns preserve approximate mobile reading position", async ({ page }) => {
  await selectObjective(page, "Objective 1.1");

  await page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    scrollTo(0, max * 0.35);
  });
  await page.waitForTimeout(120);
  const columnsRatio = await documentRatio(page);

  await page.locator("#pairBtn").click();
  await expect(page.locator("body")).toHaveClass(/pairs/);
  await page.waitForTimeout(180);
  const cardsRatio = await documentRatio(page);
  expect(Math.abs(cardsRatio - columnsRatio)).toBeLessThan(0.16);

  await page.locator("#pairBtn").click();
  await expect(page.locator("body")).not.toHaveClass(/pairs/);
  await page.waitForTimeout(180);
  const columnsAgain = await documentRatio(page);
  expect(Math.abs(columnsAgain - cardsRatio)).toBeLessThan(0.16);
});

test("visible interactive controls have accessible names and IDs stay unique", async ({ page }) => {
  const audit = await page.evaluate(() => {
    const ids = [...document.querySelectorAll("[id]")].map(element => element.id);
    const duplicates = [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))];

    const visible = element => {
      const style = getComputedStyle(element);
      const rect = element.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && rect.width > 0 && rect.height > 0;
    };
    const labelledBy = element => (element.getAttribute("aria-labelledby") || "")
      .split(/\s+/)
      .filter(Boolean)
      .map(id => document.getElementById(id)?.textContent || "")
      .join(" ");
    const accessibleName = element => [
      element.getAttribute("aria-label"),
      labelledBy(element),
      element.labels ? [...element.labels].map(label => label.textContent).join(" ") : "",
      element.getAttribute("title"),
      element.getAttribute("placeholder"),
      element.textContent
    ].filter(Boolean).join(" ").trim();

    const unnamed = [...document.querySelectorAll("button,summary,select,input,textarea")]
      .filter(visible)
      .filter(element => !accessibleName(element))
      .map(element => element.id || element.outerHTML.slice(0, 120));

    return { duplicates, unnamed };
  });

  expect(audit.duplicates).toEqual([]);
  expect(audit.unnamed).toEqual([]);
});

test("capture mobile reader, menu, and focus screenshots", async ({ page }, testInfo) => {
  await selectObjective(page, "Objective 1.1");

  const dir = path.join(process.cwd(), "artifacts", "mobile-screenshots");
  fs.mkdirSync(dir, { recursive: true });
  const prefix = testInfo.project.name;

  await page.screenshot({ path: path.join(dir, `${prefix}-reader.png`) });

  const details = page.locator("details.more-menu");
  await details.locator("summary").click();
  await page.screenshot({ path: path.join(dir, `${prefix}-more-menu.png`) });
  await page.keyboard.press("Escape");

  await details.locator("summary").click();
  await page.locator("#focusLineBtn").click();
  await page.keyboard.press("Escape");
  await page.evaluate(() => {
    const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
    scrollTo(0, max * 0.35);
  });
  await page.waitForTimeout(160);
  await page.screenshot({ path: path.join(dir, `${prefix}-reading-focus.png`) });
});
