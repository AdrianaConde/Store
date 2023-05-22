export interface Order {
  amount: number;
  client_id: number;
  supplier_id: number;
  products: Array<number>;
}
