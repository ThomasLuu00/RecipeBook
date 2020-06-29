import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Observable } from 'rxjs';

import { ApiService } from '../api/api.service';
import { Ingredient } from '../ingredient';

@Component({
  selector: 'app-ingredient-list',
  templateUrl: './ingredient-list.component.html',
  styleUrls: ['./ingredient-list.component.css']
})
export class IngredientListComponent implements OnInit {
  ingredients$: Observable<Ingredient[]>;
  ingredient_form: FormGroup;

  constructor(private apiService: ApiService, private form_builder: FormBuilder) { }

  ngOnInit(): void {
    this.getIngredients();
    this.ingredient_form = this.form_builder.group({
      name: '',
      description: '',
    });
    // Set validators for fields.
    this.ingredient_form.controls["name"].setValidators([Validators.required]);
    this.ingredient_form.controls["description"].setValidators([Validators.required]);
  }

  onSubmit() {
    // Create the Task.
    this.apiService.postIngredient(this.ingredient_form.value)
      .subscribe(
        (response) => {
          console.log(response);
          this.getIngredients();
        }
      )
  }

  public getIngredients() {
    this.ingredients$ = this.apiService.getIngredients();
  }

  public getIngredient() {
    console.log(this.apiService.getIngredient(1));
  }

  public putIngredient(ingredient: Ingredient) {
    this.apiService.putIngredient(ingredient).subscribe(
      (response) => {
        this.getIngredients();
      }
    );
  }

  public deleteIngredient(id: number) {
    this.apiService.deleteIngredient(id).subscribe(
      (response) => {
        this.getIngredients();
      }
    );
  }
}
