function openOrSenior(data){
    let memberType = []
    for (let i = 0; i < data.length; i++) {
      if ((data[i][0] >= 55) && (data[i][1] > 7)){
        memberType.push('Senior')
      }
      else {
        memberType.push('Open')
      }
    }
    return memberType
  }