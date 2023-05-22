import { Component, Input } from '@angular/core';
import { ProductCard } from 'src/app/models/Product.Interface';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css'],
})
export class CardComponent {
  @Input('product') product: ProductCard = {} as ProductCard;
}
