import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from './auth/auth.guard';
import { CallbackComponent } from './callback/callback.component';
import { IngredientListComponent } from './ingredient-list/ingredient-list.component';

const routes: Routes = [
  {
    path: 'ingredients',
    component: IngredientListComponent,
    canActivate: [ AuthGuard ]
  },
  {
    path: 'callback', component: CallbackComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [AuthGuard],
})

export class AppRoutingModule { }
