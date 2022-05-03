import {LitElement, css, html} from 'https://cdn.skypack.dev/lit';

export class MxMenu extends LitElement {
    static properties = {
        links: {},
    };

    constructor() {
        super();
        this.links = [
            {'name': 'Pickles', 'link': '/pickles'},
            {'name': 'New Pickle', 'link': '/pickles/new'},
            {'name': 'About', 'link': '/pickles/about'}
        ];
    }

    render() {
        return html`
            <details>
                <summary>Menu</summary>
                <ul>
                    ${this.links.map((link) => {
                        return html`<ul><a href=${link.link}>${link.name}</a></ul>`;
                    })}
                </ul> 
            </details>
        `;
    }
}
customElements.define('mx-menu', MxMenu);