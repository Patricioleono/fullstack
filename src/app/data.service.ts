import { Injectable } from '@angular/core';
import { Iimages } from './models/images/Iimages';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private urlApi = 'http://127.0.0.1:8000/images/getImages'
  constructor( private http:HttpClient) { }


  getAllCats():Observable<Iimages[]>{
    return this.http.get<Iimages[]>(this.urlApi)
  }

}
