import { Clipboard, ClipboardModule } from '@angular/cdk/clipboard';
import { MatFormFieldModule } from '@angular/material/form-field';
import { HeaderComponent } from '../header/header.component';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { HighlightModule } from 'ngx-highlightjs';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {ScrollingModule} from '@angular/cdk/scrolling';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [MatFormFieldModule, 
            HighlightModule, 
            MatButtonModule, 
            ScrollingModule,
            ClipboardModule,
            HeaderComponent,
            MatInputModule, 
            MatCardModule, 
            MatIconModule, 
            CommonModule, 
            FormsModule],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.css'
})
@Injectable()
export class MainPageComponent {
  public description = "";
  title = 'front-end';
  result = '';
  constructor(private clipboard: Clipboard, private http: HttpClient) {}

  copyToClipboard(value: string): void {
    this.clipboard.copy(value); 
  }

  getResult() {
    this.http.post<any>('https://uics-1-3.onrender.com/conversions', {description: this.description})
     .subscribe(data => {
      console.log(data);
      this.result = data.message.replaceAll(" ", "\n").replaceAll('\n\n', '\n');});
  }


  reset() {
    this.result = '';
    this.description = '';
  }
}
