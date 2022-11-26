def find_short(s)
    s = s.split(' ')
    l = s[0].length
    i = 0
    while i < s.length do
      if s[i].length < l
          l = s[i].length
      end
      i +=1
    end
return l
end