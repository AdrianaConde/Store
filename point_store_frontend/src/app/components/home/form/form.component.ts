import { Component } from '@angular/core';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css'],
})
export class FormComponent {
  isAuth: boolean = true;
  type: string = 'proveedor';
  successStatus = '';
  public updateAuth(auth: boolean, typeInsert: string) {
    this.isAuth = auth;
    this.type = typeInsert;
  }
  public successSave(event: any) {
    if (event === 'success') {
      this.isAuth = true;
      this.successStatus = event;
    }
  }
}
