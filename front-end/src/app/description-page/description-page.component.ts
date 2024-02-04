import { HeaderComponent } from '../header/header.component';
import { MatCardModule } from '@angular/material/card';
import { MatTreeModule, MatTreeNestedDataSource} from '@angular/material/tree';
import { MatIconModule } from '@angular/material/icon';
import { Component, ContentChild, Input } from '@angular/core';
import { NestedTreeControl, getTreeControlFunctionsMissingError } from '@angular/cdk/tree';
import { MatButtonModule } from '@angular/material/button';
import { Title } from '@angular/platform-browser';
import { RouterLinkWithHref } from '@angular/router';
import { ListKeyManager } from '@angular/cdk/a11y';
import { isNgTemplate } from '@angular/compiler';

interface ComponentNode {
  name: string;
  children?: ComponentNode[];
}

const TREE_DATA: ComponentNode[] = [
  {
    name: 'Header',
    children: [{name: 'Title'}, {name: 'Paragraph'}]
  },
  {
    name: 'Content',
    children: [
      {
        name: 'Card',
        children: [
          {name: 'Card Header', children: [{name: "Card Title"}, {name: "Card Subtitle"}]}, 
          {name: 'Card Content', children:[{name: "Grid", children: [{name: "Row", children: [{name: "Column"}]}]}, {name: "Image"}, {name: "Input"}, {name: "Button"}, {name: "List", children:[{name: "Item"}]}]}
        ]
      },
      {name: 'Grid', children: [{name: "Row", children: [{name: "Column"}]}]},
      {name: "Image"},
      {name: "Input"},
      {name: "Paragraph"},
      {name: "Button"},
      {name: "List", children:[{name: "Item"}]}
    ],
  },
  {
    name: 'Footer',
    children: [{name: 'Paragraph'}]
  }
];


@Component({
  selector: 'app-description-page',
  standalone: true,
  imports: [HeaderComponent,
            MatButtonModule,
            MatIconModule,
            MatTreeModule,
            MatCardModule],
  templateUrl: './description-page.component.html',
  styleUrl: './description-page.component.css'
})
export class DescriptionPageComponent {
  treeControl = new NestedTreeControl<ComponentNode>(node => node.children);
  dataSource = new MatTreeNestedDataSource<ComponentNode>();

  constructor() {
    this.dataSource.data = TREE_DATA;
  }

  hasChild = (_: number, node: ComponentNode) => !!node.children && node.children.length > 0;
}
