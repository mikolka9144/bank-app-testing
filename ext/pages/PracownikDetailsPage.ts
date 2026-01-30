import { Page, expect } from '@playwright/test';

export class PracownikDetailsPage {
  constructor(private page: Page) {}

  async expectRoomNumber(room: string) {
    await expect(this.page.getByText(`Nr pokoju: ${room}`)).toBeVisible();
  }
  async expectToWorkIn(group: string) {
    await expect(this.page.getByText(group)).toBeVisible();
  }
}
