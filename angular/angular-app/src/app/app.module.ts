import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import {MatExpansionModule} from '@angular/material/expansion'; 
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner'; 
import {MatInputModule} from '@angular/material/input'; 
import {MatIconModule} from '@angular/material/icon';
import {MatSidenavModule} from '@angular/material/sidenav';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IngredientListComponent } from './ingredient-list/ingredient-list.component';

import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavbarComponent } from './navbar/navbar.component';
import { BannerComponent } from './banner/banner.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HomepageComponent } from './homepage/homepage.component';
import { TechniqueListComponent } from './technique-list/technique-list.component';
import { StickyFloatDirective } from './directives/sticky-float.directive';
import { ContentBarComponent } from './content-bar/content-bar.component';
import { SentinelObserverDirective } from './directives/sentinel-observer.directive';

@NgModule({
  declarations: [
    AppComponent,
    IngredientListComponent,
    NavbarComponent,
    BannerComponent,
    DashboardComponent,
    HomepageComponent,
    TechniqueListComponent,
    StickyFloatDirective,
    ContentBarComponent,
    SentinelObserverDirective,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,

    // Material UI imports
    MatExpansionModule,
    MatToolbarModule,
    MatButtonModule,
    MatProgressSpinnerModule,
    MatInputModule,
    MatIconModule,
    MatSidenavModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
