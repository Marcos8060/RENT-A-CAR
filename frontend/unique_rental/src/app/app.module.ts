import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Routes, RouterModule } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeroComponent } from './hero/hero.component';
import { FleetComponent } from './fleet/fleet.component';
import { DetailsComponent } from './details/details.component';
import { ProfileComponent } from './profile/profile.component';


const appRoutes: Routes = [
  { path: '' , component : HeroComponent },
  { path: 'fleet', component : FleetComponent},
  { path: 'details', component: DetailsComponent},
  { path: 'profile', component: ProfileComponent}
]
@NgModule({
  declarations: [
    AppComponent,
    HeroComponent,
    FleetComponent,
    DetailsComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
