import { Page, expect } from '@playwright/test';

export class SkladOsobowyPage {
  constructor(private page: Page) {}

  async searchByName(name: string) {
    await this.page.getByLabel('Imię lub nazwisko').fill(name);
    await this.page.locator('#edit-submit-pracownik-szukaj').click();
  }

  async openEmployee(fullName: string) {
    const link = this.page.getByRole('link', { name: fullName });
    await expect(link).toBeVisible();
    await link.click();
  }
}
