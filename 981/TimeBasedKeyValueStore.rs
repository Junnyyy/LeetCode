use std::collections::{BTreeMap, HashMap};

struct TimeMap {
    map: HashMap<String, BTreeMap<i32, String>>,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            map: HashMap::new(),
        }
    }
    
    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.map
            .entry(key)
            .or_insert_with(BTreeMap::new)
            .insert(timestamp, value);
    }
    
    fn get(&self, key: String, timestamp: i32) -> String {
        if let Some(tree) = self.map.get(&key) {
            if let Some((_t, v)) = tree.range(..=timestamp).next_back() {
                return v.clone();
            }
        }
        String::new()
    }
}
