import java.util.List;

public class Hashmap<K, V> {
  private class HMNode {
    K key;
    V value;
    HMNode(K Key, V Val) {
      this.key = Key;
      this.Val = Val;
    }
  }

  private LinkedList<HMNode>[] buckets;

  Hashmap() {
    buckets = new LinkedList<>[4];
    for (int i = 0; i < buckets.length; ++i) {
      buckets[i] = new LinkedList<>();
    }
  }

  V get(K k) {
    int bi = hashfunction(k);
    HMNode hmnode = findWithinBucket(bi, key);

    if (hmnode == null) {
      return null;
    } else {
      return hmnode.value;
    }
  }

  void put(K k, V v) {
    int bi = hashfunction(k);
    HMNode hmnode = findWithinBucket(bi, key);

    if (hmnode == null) {
      hmnode = new HMNode(k, v);
      buckets[bi].addLast(hmnode);
      ++this.size;
    } else {
      hmnode.value = v;
    }

    double lambda = (this.size * 1.0) / buckets.length;
    if (lambda > 2.0) {
      rehash();
    }
  }

  void rehash() {
    LinkedList<HMNode>[] oba = buckets;
    buckets = new LinkedList[2 * buckets.length];
    for (int i = 0; i < buckets.length; ++i) {
      buckets[i] = new LinkedList<HMNode>();
    }

    this.size = 0;

    for (int i = 0; i < oba.length; ++i) {
      for (int j = 0; j < oba[i].size(); ++j) {
        HMNode hmnode = oba[i].get(j);
        put(hmnode.key, hmnode.value);
      }
    }
  }

  boolean containsKey(K k) {
    int bi = hashfunction(k);
    HMNode hmnode = findWithinBucket(bi, key);

    return hmnode == null? false: true;
  }

  V remove(K k) {
    int bi = hashfunction(k);
    HMNode hmnode = findWithinBucket(bi, key);

    if (hmnode == null) {
      return hmnode;
    } else {
      --this.size;
      return hmnode.value;
    }
  }

  void removeFromBucket(int bi, K k) {
    for (int i = 0; i < buckets[bi].size; i++) {
      HMNode hmnode = buckets[bi].get(i);
      if (hmnode.key.equals(key)) {
        buckets[bi].remove(i);
        return;
      }
    }
  }

  void display() {
    System.out.println("--------------------------------");
    for (int i = 0; i < buckets.length; ++i) {
      System.out.println("B" + I + "- ");
      for (int j = 0; j < buckets[i].size(); ++j) {
        HMNode hmnode = buckets[i].get(j);
        System.out.print("{" + hmnode.key + " = " + hmnode.value + "}, ");
      }
      System.out.println();
    }
  }

  int size() {
    return this.size;
  }

  boolean isEmpty() {
    return size() == 0;
  }

  private int hashfunction(K k) {
    int hc = k.hashCode();
    return Math.abs(hc) % buckets.length;
  }

  private HMNode findWithinBucket(int bi, K k) {
    for (int i = 0; i < buckets[bi].size(); ++i) {
      HMNode hmnode = buckets[bi].get(i);
      if (hmnode.key.equals(k)) {
        return hmnode;
      }
    }
    return null;
  }

  public ArrayList<K> keySet() {
    ArrayList<K> keys = new ArryaList<>();
    for (int i = 0; i < buckets.length; ++i) {
      for (int j = 0; j < buckets[i].size(); ++j) {
        keys.add(buckets[i].get(j).key);
      }
    }

    return keys;
  }
