const fibbin = (targetIndex) => {
    if (targetIndex < 2) {
        return targetIndex;
    }
    
    return fibbin(targetIndex - 1) + fibbin(targetIndex - 2);
}

console.log(fibbin(6));