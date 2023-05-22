import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './views/home/home.component';
import { ProveedorComponent } from './views/proveedor/proveedor.component';
import { ClienteComponent } from './views/cliente/cliente.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
  },
  {
    path: 'proveedor/:id',
    component: ProveedorComponent,
  },
  {
    path: 'client/:id',
    component: ClienteComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
