import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { CurrencySelectorComponent } from './currency-selector/currency-selector.component'; // Adjust the path as needed

@NgModule({
  declarations: [
    AppComponent,
    CurrencySelectorComponent // Declare the component
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
