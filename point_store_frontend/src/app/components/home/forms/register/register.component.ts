import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { APIService } from 'src/app/services/api.service';
import { Supplier } from 'src/app/models/Supplier.interface';
import { Client } from 'src/app/models/client.interface';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
})
export class RegisterComponent {
  typeRegisterLabel: string = 'Proveedor';
  @Input('typeRegister') typeRegister = 'proveedor';
  @Output('success') success = new EventEmitter();
  public formRegister = new FormGroup({
    name: new FormControl(''),
    last_name: new FormControl(''),
    cedula: new FormControl(''),
    address: new FormControl(''),
    telephone: new FormControl(''),
  });

  constructor(private api: APIService) {}
  getTypeRegister() {
    return this.typeRegister === 'proveedor' ? 'Proveedor' : 'Cliente';
  }

  public onSubmit() {
    let supplier: Supplier;
    let client: Client;
    console.log('Data');
    if (this.typeRegister === 'proveedor') {
      supplier = {
        name: this.formRegister.get('name')?.value?.toString() || '',
        telephone: this.formRegister.get('telephone')?.value?.toString() || '',
        address: this.formRegister.get('address')?.value?.toString() || '',
        cedula: this.formRegister.get('cedula')?.value?.toString() || '',
      };
      console.log(supplier);
      this.api.createSupplier(supplier).subscribe((response) => {
        console.log('created_success');
        this.success.emit('success');
      });
    } else {
      client = {
        name: this.formRegister.get('name')?.value?.toString() || '',
        last_name: this.formRegister.get('last_name')?.value?.toString() || '',
        telephone: this.formRegister.get('telephone')?.value?.toString() || '',
        address: this.formRegister.get('address')?.value?.toString() || '',
        cedula: this.formRegister.get('cedula')?.value?.toString() || '',
      };
      console.log(client);
      this.api.createClient(client).subscribe((response) => {
        console.log('created_success');
        this.success.emit('success');
      });
    }
  }
}
