import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'

import { AppComponent } from './app.component';
import { ImagenesComponent } from './imagenes/imagenes.component';
import { GatitosComponent } from './gatitos/gatitos.component';
import { RouterModule} from '@angular/router';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeComponent } from './home/home.component'

@NgModule({
  declarations: [
    AppComponent,
    ImagenesComponent,
    GatitosComponent,
    NavbarComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot([
      {path: 'imagenes', component:ImagenesComponent},
      {path: 'gatitos', component:GatitosComponent},
      {path: '', component:HomeComponent},
      {path: '**',redirectTo:'/', pathMatch:'full'}
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
