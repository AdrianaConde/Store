import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductCard } from 'src/app/models/Product.Interface';
import { SupplierCard } from 'src/app/models/Supplier.interface';
import { APIService } from 'src/app/services/api.service';

@Component({
  selector: 'app-proveedor',
  templateUrl: './proveedor.component.html',
  styleUrls: ['./proveedor.component.css'],
})
export class ProveedorComponent {
  public productCards = new Array<ProductCard>();
  public proveedor: SupplierCard = {} as SupplierCard;
  constructor(private route: ActivatedRoute, private api: APIService) {}
  ngOnInit() {
    let id = this.route.snapshot.paramMap.get('id');
    this.api.getProveedor(id || '').subscribe((result) => {
      this.proveedor = result as SupplierCard;
      this.productCards = this.proveedor.products;
    });
  }
  onSaveNewProduct(event: any) {
    console.log('save successsss');
    let id = this.route.snapshot.paramMap.get('id');
    this.api.getProveedor(id || '').subscribe((result) => {
      this.proveedor = result as SupplierCard;
      this.productCards = this.proveedor.products;
    });
  }
}
