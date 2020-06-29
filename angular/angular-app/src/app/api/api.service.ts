import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs';
import { Ingredient } from '../ingredient';
import { AuthService } from '../auth/auth.service';

@Injectable({
  providedIn: 'root'
})

export class ApiService {
  API_URL = 'http://localhost/api/v1';

  constructor(private http: HttpClient, private auth: AuthService) {}

  public getIngredients() : Observable<Ingredient[]> {
    return this.http.get<Ingredient[]>(`${this.API_URL}/ingredients`,
    {
      headers: new HttpHeaders().set('Authorization', `Bearer ${this.auth.accessToken}`)
    });
  }

  public postIngredient(ingredient: Ingredient) {
    return this.http.post<Ingredient>(`${this.API_URL}/ingredients/`, ingredient,
    {
      headers: new HttpHeaders().set('Authorization', `Bearer ${this.auth.accessToken}`)
    });
  }

  public getIngredient(id: number) {
    return this.http.get<Ingredient>(`${this.API_URL}/ingredient/${id}/`,
    {
      headers: new HttpHeaders().set('Authorization', `Bearer ${this.auth.accessToken}`)
    });
  }

  public putIngredient(ingredient: Ingredient) {
    return this.http.put<Ingredient>(`${this.API_URL}/ingredient/${ingredient.id}/`, ingredient,
    {
      headers: new HttpHeaders().set('Authorization', `Bearer ${this.auth.accessToken}`)
    });
  }

  public deleteIngredient(id: number) {
    return this.http.delete(`${this.API_URL}/ingredient/${id}/`,
    {
      headers: new HttpHeaders().set('Authorization', `Bearer ${this.auth.accessToken}`)
    });
  }
}
