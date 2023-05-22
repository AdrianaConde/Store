import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './views/home/home.component';
import { ImagePresentComponent } from './components/home/image-present/image-present.component';
import { RegisterComponent } from './components/home/forms/register/register.component';
import { AuthComponent } from './components/home/forms/auth/auth.component';
import { FormComponent } from './components/home/form/form.component';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { ProveedorComponent } from './views/proveedor/proveedor.component';
import { ClienteComponent } from './views/cliente/cliente.component';
import { CardComponent } from './components/card/card.component';
import { ProductComponent } from './components/product/product.component';
import { OrderComponent } from './views/order/order.component';
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ImagePresentComponent,
    RegisterComponent,
    AuthComponent,
    FormComponent,
    ProveedorComponent,
    ClienteComponent,
    CardComponent,
    ProductComponent,
    OrderComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
