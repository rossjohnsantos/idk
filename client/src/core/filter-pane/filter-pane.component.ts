import { Component, OnInit } from '@angular/core';
import { StocksService } from '../data/stocks.service';
import { FilterService } from "primeng/api";

@Component({
  selector: 'app-filter-pane',
  templateUrl: './filter-pane.component.html',
  styleUrls: ['./filter-pane.component.scss'],
  providers: [StocksService, FilterService]
})
export class FilterPaneComponent implements OnInit {

  selectedTicker: any;
  tickers: any = [ ];
  filteredTickers: any = [];

  constructor(public ss: StocksService) {
    this.ss.getStocks().subscribe(stocks => {
     for (const ticker of stocks) {
       this.tickers.push(ticker['Symbol'] + ': ' + ticker['Company Name']);
     }
     console.log(this.tickers)
    })
   }

  ngOnInit(): void {
  }

  filterStock(event: { query: any; }): void {
    let filtered: any[]= [];
    let query = event.query;
    for (let i = 0; i < this.tickers.length; i++) {
      let ticker = this.tickers[i];
      if (ticker.toLowerCase().indexOf(query.toLowerCase()) == 0) {
        filtered.push(ticker);
      }
    }
    this.filteredTickers = filtered;
  }
}
