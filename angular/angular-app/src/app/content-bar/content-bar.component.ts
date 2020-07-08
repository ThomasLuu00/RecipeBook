import { Component, OnInit, HostListener } from '@angular/core';

@Component({
  selector: 'app-content-bar',
  templateUrl: './content-bar.component.html',
  styleUrls: ['./content-bar.component.css']
})
export class ContentBarComponent implements OnInit {

  isStuck = false;

  constructor() { }

  ngOnInit(): void {
  }

}
