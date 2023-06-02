import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'imagenes',
  templateUrl: './imagenes.component.html',
  styleUrls: ['./imagenes.component.css']
})
export class ImagenesComponent implements OnInit {

  constructor(private http:HttpClient){}

  ngOnInit(){

   this.http.get('http://127.0.0.1:8000/images/getImages').subscribe( data => console.log(data))
  }

}
