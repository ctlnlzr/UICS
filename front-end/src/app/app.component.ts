import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Clipboard, ClipboardModule } from '@angular/cdk/clipboard';
import { RouterModule, Routes } from '@angular/router';
import { trigger, state, style, animate, transition } from '@angular/animations';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,ClipboardModule,CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  animations: [
    trigger('fadeInOut', [
      state('void', style({
        opacity: 0,
      })),
      transition(':enter', [
        animate(500, style({
          opacity: 1,
        })),
      ]),
      transition(':leave', [
        animate(500, style({
          opacity: 0,
        })),
      ]),
    ]),
  ]
})

export class AppComponent {
  title = 'front-end';
  code = '<div class = "test"> \n   <p>Test</p>\n</div>';
  constructor(private clipboard: Clipboard) {}

  copyToClipboard(value: string): void {
    this.clipboard.copy(value); 
  }

  isDivVisible = false;
  toggleDivVisibility() {
    this.isDivVisible = !this.isDivVisible;
  }
}
