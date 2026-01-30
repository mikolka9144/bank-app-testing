import { test, expect } from '@playwright/test';

test('Wyszukiwanie pracownika Sołtysa i sprawdzenie szczegółów', async ({ page }) => {
  // 1. Otwórz stronę
  await page.goto('https://mfi.ug.edu.pl/');

  // 2. Kliknij guzik "Pracownicy"
  await page.getByLabel('Nagłówek').getByRole('link', { name: 'Pracownicy' }).click();

  // 3. Kliknij odnośnik "skład osobowy"
  await page.getByLabel('Pracownicy').getByRole('link', { name: 'skład osobowy' }).click();

  // 4. Wyszukaj pracowników o nazwisku "sołtys"
  await page.getByLabel('Imię lub nazwisko').fill('sołtys');
  
  await page.locator('#edit-submit-pracownik-szukaj').click();

  // Upewnij się, że link "mgr Konrad Sołtys" jest widoczny
  const link = page.getByRole('link', { name: 'mgr Konrad Sołtys' });
  await expect(link).toBeVisible();

  // 5. Kliknij link
  await link.click();

  // 6. Sprawdź, czy tekst "Nr pokoju: 4.19" jest wyświetlony
  await expect(page.getByText('Nr pokoju: 4.19')).toBeVisible();
});
