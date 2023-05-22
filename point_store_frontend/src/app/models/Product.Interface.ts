export interface Product {
  name: String;
  price: number;
  descripcion: String;
  supplier_id?: String;
  amount: number;
}
export interface ProductCard {
  id: number;
  name: String;
  price: number;
  amount: number;
  descripcion: String;
  supplier_id?: String;
}
export interface CounProductCard {
  product: ProductCard;
  count: number;
}
