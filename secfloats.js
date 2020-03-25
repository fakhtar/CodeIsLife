my_strings = ['5','12.01',
'.01',
'.1',
'12.00',
'12.1',
'12.21',
'12.20',
'1.01',
'1.1',
'1.21',
'1.20',
'01.01',
'01.1',
'01.21',
'01.20',
'00.01',
'00.1',
'00.21',
'00.20',
'0.01',
'0.1',
'0.21',
'0.20'
]

function set_person_month(element) {
    if (!element.includes(".")) {
        element = element.concat('.00')
    }
    first_part = element.toString().split('.')[0]
    sec_part = element.toString().split('.')[1]
    if (first_part.length == 0) {
        first_part = '0';
        
    }
    else if (first_part.length == 2) {
        first_part = parseFloat(first_part).toString();
    }

    if (sec_part.length == 0) {
        sec_part = '00'
    }
    else if (sec_part.length == 1) {
        sec_part = sec_part + '0'
    }
    return first_part + '.' + sec_part
}

my_strings.forEach(element => {
    console.log('-------');
    console.log(set_person_month(element));
    console.log('-------');
});