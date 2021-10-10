import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StocksService {

  private _stockJson = 'assets/stocks.json';

  constructor(private http: HttpClient) {}

  public getStocks(): Observable<any> {
    return this.http.get<any>(this._stockJson);
  }
}
