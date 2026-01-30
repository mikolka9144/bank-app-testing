import { test } from '@playwright/test';
import { HomePage } from '../pages/HomePage';
import { PracownicyPage } from '../pages/PracownicyPage';
import { SkladOsobowyPage } from '../pages/SkladOsobowyPage';
import { PracownikDetailsPage } from '../pages/PracownikDetailsPage';

test('Wyszukiwanie pracownika Sołtysa i sprawdzenie szczegółów', async ({ page }) => {
  const home = new HomePage(page);
  const pracownicy = new PracownicyPage(page);
  const sklad = new SkladOsobowyPage(page);
  const details = new PracownikDetailsPage(page);

  await home.goto();
  await home.openPracownicy();

  await pracownicy.openSkladOsobowy();

  await sklad.searchByName('sołtys');
  await sklad.openEmployee('mgr Konrad Sołtys');

  await details.expectRoomNumber('4.19');
});
