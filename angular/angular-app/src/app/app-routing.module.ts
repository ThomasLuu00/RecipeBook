import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from './auth/auth.guard';
import { CallbackComponent } from './callback/callback.component';
import { IngredientListComponent } from './ingredient-list/ingredient-list.component';
import { HomepageComponent } from './homepage/homepage.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TechniqueListComponent } from './technique-list/technique-list.component';

const routes: Routes = [
  {
    path: 'home',
    component: HomepageComponent,
  },
  {
    path: 'dashboard',
    children:[
      {
        path: '',
        component: DashboardComponent,
        //canActivate: [ AuthGuard ]
      },
      {
        path: 'ingredients',
        component: IngredientListComponent,
        //canActivate: [ AuthGuard ]
      },
      {
        path: 'techniques',
        component: TechniqueListComponent,
      },
    ]
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
