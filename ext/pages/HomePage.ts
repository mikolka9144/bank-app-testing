import { Page } from '@playwright/test';

export class HomePage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('https://mfi.ug.edu.pl/');
  }

  async openPracownicy() {
    await this.page.getByLabel('Nagłówek').getByRole('link', { name: 'Pracownicy' }).click();
  }
}
