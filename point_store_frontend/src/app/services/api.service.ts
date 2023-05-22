import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Supplier } from '../models/Supplier.interface';
import { Client } from '../models/client.interface';
import { Product } from '../models/Product.Interface';
import { Order } from '../models/Orders.interface';
@Injectable({
  providedIn: 'root',
})
export class APIService {
  url_base = 'http://localhost:5000/';
  constructor(private httpClient: HttpClient) {}

  public createClient(body: Client) {
    return this.httpClient.post(`${this.url_base}createClient`, body);
  }

  public createSupplier(body: Supplier) {
    return this.httpClient.post(`${this.url_base}createSupplier`, body);
  }

  public createProduct(body: Product) {
    return this.httpClient.post(`${this.url_base}createProduct`, body);
  }
  public getUser(cedula: string) {
    return this.httpClient.get(`${this.url_base}getSupplierDNI/${cedula}`);
  }
  public getProveedor(id: string) {
    return this.httpClient.get(`${this.url_base}getSupplier/${id}`);
  }
  public getProduct() {
    return this.httpClient.get(`${this.url_base}getProduct`);
  }
  public createOrder(body: Order) {
    return this.httpClient.post(`${this.url_base}createOrder`, body);
  }
  public getOrder(){
    return this.httpClient.get(`${this.url_base}getOrder`);
  }
}
