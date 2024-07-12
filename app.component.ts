import { Component } from '@angular/core';
import { Currency } from './currency-selector/currency.model'; // Adjust the path as needed

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  availableCurrencies: Currency[] = [
    { code: 'USD', name: 'US Dollar', rate: 1.0 },
    { code: 'EUR', name: 'Euro', rate: 0.9 },
    // Add more currencies as needed
  ];

  handleCurrencySelect(selectedCurrency: Currency) {
    console.log('Selected currency:', selectedCurrency);
    // Handle the selected currency here
  }
}
