import { Page } from '@playwright/test';

export class PracownicyPage {
  constructor(private page: Page) {}

  async openSkladOsobowy() {
    await this.page.getByLabel('Pracownicy').getByRole('link', { name: 'skład osobowy' }).click();
  }
}
