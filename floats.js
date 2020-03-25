my_strings = ['12.01',
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
'0.20',
'5']

my_strings.forEach(element => {
    console.log(parseFloat(element));
    console.log('Test again regex');
    console.log(/^\d{1,2}(\.\d{1,2})?$/.test(element));
    console.log('Test if contains decimal');
    console.log(element.includes("."));
    if (!element.includes(".")) {
        console.log('Append .00');
        console.log(element.concat('.00'));        
    } else {
        if (parseFloat(element).toString().split('.')[1].length == 2) {
                console.log('do nothing');
                console.log(parseFloat(element));
        } else if (parseFloat(element).toString().split('.')[1].length == 1) {
                console.log('Append 0');
                console.log(parseFloat(element).toString().concat('0')); 
        }
    }     
    console.log('------------------');
    
});