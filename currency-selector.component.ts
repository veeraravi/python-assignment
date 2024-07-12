import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Currency } from './currency.model';

@Component({
  selector: 'app-currency-selector',
  templateUrl: './currency-selector.component.html',
  styleUrls: ['./currency-selector.component.css']
})
export class CurrencySelectorComponent {
  @Input() currencies: Currency[];
  @Output() onSelect: EventEmitter<Currency> = new EventEmitter();

  constructor() { }

  onCurrencyChange(event: any) {
    const selectedCurrency = this.currencies[event.target.selectedIndex];
    this.onSelect.emit(selectedCurrency);
  }
}
