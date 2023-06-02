export interface Iimages{
    breeds:      any[];
    categories?: Category[];
    id:          string;
    url:         string;
    width:       number;
    height:      number;
}

export interface Category {
    id:   number;
    name: string;
}