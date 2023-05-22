import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Product } from 'src/app/models/Product.Interface';
import { APIService } from 'src/app/services/api.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css'],
})
export class ProductComponent {
  registerProduct = new FormGroup({
    name: new FormControl(''),
    descripcion: new FormControl(''),
    price: new FormControl(''),
    amount: new FormControl(),
  });
  @Input('id') id: number = 0;
  @Output('success') success = new EventEmitter();
  constructor(private api: APIService) {}

  onSubmit() {
    const product: Product = {
      descripcion: this.registerProduct.get('descripcion')?.value || '',

      name: this.registerProduct.get('name')?.value || '',

      price: parseFloat(this.registerProduct.get('price')?.value || '0'),

      amount: parseInt(this.registerProduct.get('amount')?.value || ''),
      supplier_id: this.id.toString(),
    };
    this.api.createProduct(product).subscribe((result) => {
      console.log('event');
      this.success.emit('success');
    });
  }
}
