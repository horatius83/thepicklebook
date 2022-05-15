import {LitElement, html} from 'https://cdn.skypack.dev/lit';

export class MxPickleMenu extends LitElement {
    static properties = {
        pickleMakers: {type: Array},
        pickles: {type: Array}
    };
    pickleMakerEndpoint = '/pickles/manufactuer/all';
    getPickleEndpoint = (id) => `/pickles/manufacturer/${id}/pickles`;

    constructor() {
        super();
        this.pickleMakers = [];
        this.pickles = [];
    }

    onLoad = async () => {
        try {
            const result = await fetch(this.pickleMakerEndpoint, {
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });
            this.pickleMakers = await result.json();
            this.pickleMakers.sort((a, b) => a.name.localeCompare(b.name));
        } catch (e) {
            console.error(e);
        }
    }

    connectedCallback() {
        super.connectedCallback();
        window.addEventListener('load', this.onLoad);
    }

    disconnectedCallback() {
        window.removeEventListener('load', this.onLoad);
        super.disconnectedCallback();
    }

    makerChanged(e) {
        const id = e.target.value;
        const pickleEndpoint = this.getPickleEndpoint(id);
        fetch(pickleEndpoint, {
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then((result) => result.json())
        .then((pickles) => {
            this.pickles = pickles;
            this.pickles.sort((a, b) => a.name.localeCompare(b.name));
        })
        .catch((e) => console.error(e));
    }

    render() {
        return html`
            <link rel="stylesheet" href="/pickles/static/css/mini-css/3.0.1/mini-default.min.css" />
            <div class="input-group vertical">
                <label for="pickler_maker">Manufacturer</label>
                <select name="pickle_maker" id="pickle_maker" @change=${this.makerChanged}>
                    ${this.pickleMakers.map((e) => {
                        return html`<option value=${e.id}>${e.name}</option>`
                    })}
                </select>
            </div>
            <div class="input-group vertical">
                <label for="pickles">Pickle</label>
                <select name="pickles" id="pickles">
                    ${this.pickles.map((e) => {
                        return html`<option value=${e.id}>${e.name}</option>`
                    })}
                </select>
            </div>
        `;
    }
}
customElements.define('mx-picklemenu', MxPickleMenu);