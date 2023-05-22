import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { User } from 'src/app/models/user.interface';
import { APIService } from 'src/app/services/api.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
})
export class AuthComponent {
  form = new FormGroup({
    cedula: new FormControl(''),
  });
  constructor(private route: Router, private api: APIService) {}
  onSubmit() {
    const cedula = this.form.get('cedula')?.value || '';
      this.api.getUser(cedula).subscribe((result) => {
        console.log(result);
        const resultData = result as User;
        if (resultData.type === 'proveedor') {
          this.route.navigate(['/proveedor', resultData.id]);
        } else {
          this.route.navigate(['/client', resultData.id]);
        }
      });
  }
  Error(){
    
  };
  
}
