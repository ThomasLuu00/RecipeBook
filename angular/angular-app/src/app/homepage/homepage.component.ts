import { Component, OnInit, HostListener } from '@angular/core';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
  floatContentBar = false;

  constructor() { }

  onStuck(e) {
    console.log(e)
    this.floatContentBar = true;
  }
  onUnstuck(e) {
    console.log('unstuck')
    this.floatContentBar = false;
  }

  scrollToElement($element): void {
    $element.scrollIntoView({behavior: "smooth", block: "start", inline: "nearest"});
  }

  ngOnInit(): void {}

}
