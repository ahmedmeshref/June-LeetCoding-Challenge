/**
 * @param {string} IP
 * @return {string}
 */
var validIPAddress = function(IP) {
    let ipv6 = /^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$/gi;
    if (IP.match(ipv6)){
        return "IPv6";
    }

    let ipv4 = /^(?!0)([0-9]{1,3}\.){3}(?!0)([0-9]{1,3})$/g;
    let l_ipv4 = IP.match(ipv4);
    if (l_ipv4){
        for (const num of l_ipv4[0].split(".")){
            if (0 > parseInt(num) || parseInt(num) > 255) return "Neither";
        }
        return "IPv4";
    }
    return "Neither";
};



let ip = "256.256.256.256";
console.log(validIPAddress(ip));