var geners = document.getElementById("geners");
var gen =[["Бойовик", "bojovic"], ["Військовий", "vijskovij"], ["Детектив", "detectiv"],
            ["Дитячий", "detskij"], ["Домашній", "domashnij"], ["Драма", "drama"],
            ["Історичний", "istorikal"], ["Казка", "kazka"], ["Класика", "klasika"],
            ["Комедія", "komedia"], ["Мелодрама", "melodrama"], ["Наук. фантастика", "naukfantast"],
            ["Патріотичний", "patriotichniy"], ["Пригоди", "prigodi"], ["Психологія", "psichologia"],
            ["Реалізм", "realizm"], ["Роздуми", "rozdumi"], ["Романтика", "romantica"],
            ["Спорт", "sport"], ["Триллер", "triller"], ["Жахи", "jahi"], ["Містика", "mistik"],
            ["Фантастика", "fantastik"], ["Фентезі", "fentezi"]];
//html = '<ul>';
gen.forEach(function(item, i, gen) {
//    alert( i + ": " + item[1] );
    var br = document.createElement('br');
    var a = document.createElement('a');
    var linkText = document.createTextNode(item[0]);
    a.appendChild(linkText);
    a.title = item[0];
    a.href = "http://127.0.0.1:8000/teka/"+item[1];
    geners.appendChild(a);
    geners.appendChild(br);
//  html += '<li>'+item+'</li>';
});
//html += '</ul>'