import { ProductCard } from './Product.Interface';

export interface Supplier {
  name: String;
  telephone: String;
  cedula: String;
  address: String;
}

export interface SupplierCard {
  id: number;
  type: String;
  name: String;
  telephone: String;
  cedula: String;
  address: String;
  products: Array<ProductCard>;
}
