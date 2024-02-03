import { HeaderComponent } from '../header/header.component';
import { MatCardModule } from '@angular/material/card';
import { Component } from '@angular/core';

@Component({
  selector: 'app-description-page',
  standalone: true,
  imports: [HeaderComponent,
            MatCardModule],
  templateUrl: './description-page.component.html',
  styleUrl: './description-page.component.css'
})
export class DescriptionPageComponent {

}
