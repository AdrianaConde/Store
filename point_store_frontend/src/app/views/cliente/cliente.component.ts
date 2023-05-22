import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Order } from 'src/app/models/Orders.interface';
import { CounProductCard, ProductCard } from 'src/app/models/Product.Interface';
import { APIService } from 'src/app/services/api.service';

@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.css'],
})
export class ClienteComponent {
  public productCards = new Array<ProductCard>();
  public countCard = new Array<CounProductCard>();
  constructor(private api: APIService, private route: ActivatedRoute) {}
  ngOnInit() {
    this.api.getProduct().subscribe((result) => {
      this.productCards = result as Array<ProductCard>;
    });
  }

  addCard(card: ProductCard) {
    console.log(card);
    const produc = this.countCard.find((obj) => obj.product.id === card.id);
    if (produc) {
      produc.count++;
    } else {
      this.countCard.push({
        count: 1,
        product: card,
      });
    }
  }
  pay() {
    const result = this.countCard.reduce(
      (acc: number, current: CounProductCard) => {
        acc += current.count * current.product.price;
        return acc;
      },
      0 as number
    );

    return result;
  }
  payed() {
    const ids = this.countCard.map((p) => p.product.id);
    const order: Order = {
      amount: this.pay(),
      client_id: parseInt(this.route.snapshot.paramMap.get('id') || '0'),
      supplier_id: 1,
      products: ids,
    };
    this.api.createOrder(order).subscribe((result) => {
      this.countCard = [];
    });
  }
}
