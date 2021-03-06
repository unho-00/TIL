## Java 각종 개념

#### **연산자**

* **비트연산자**

& : 비트(값)이 모두 1일때 결과 1 나머지는 0
| : 비트(값)이 하나라도 1일때 결과 1 나머지는 0

^ : 비트(값)이 서로 다를때 결과 1 나머지는 0

~ : 비트(값)이 정반대 반전 결과

<< : 명시된 수만큼 비트 전부 왼쪽 이동 (오른쪽 0으로 채워짐)

\>> : 부호 유지, 지정한 수만큼 비트 전부 오른쪽 이동 (왼쪽 양수 0으로, 음수 1로 채워짐)

\>>> : 지정한 수만큼 비트 전부 오른쪽 이동 (이외 비트 0)

* **삼항연산자**

조건식 ? 조건이 true일때 반환값 : 조건 false일때 반환값

```java
int max = num1>num2?num1:num2;
```

* **Instanceof 연산자**

인스턴스(객체)가 클래스와 인터페이스로 부터 생성되었는지를 알려줌

```java
public static void main(String[] args){
    A a = new A();
    B b = new B();
    
    boolean result1 = a instanceof A; //true
}
```





#### **overriding 과 overloading**

* **overriding**은 자식 클래스가 부모클래스의 메소드를 이용하는데 내용을 덮어쓰는 경우, 오버라이딩이라고 한다.
* **overloading**은 메소드의 반환형태와 이름이 동일하지만, 파라미터의 갯수가 다른 경우,  여러개 사용 가능하도록 하는것을 오버로딩이라 한다.



#### 접근 제어자 (public, protected, default, private)

**멤버**

* **public**은 본인 클래스외에 다른 클래스에서도 접근이 가능

* **protected**은 같은 패키지와 자손클래스까지 접근 가능
* **Default**은 아무것도 표기하지 않은 상태
  같은 패키지 내에서는 접근 가능, **Default**는 붙이지 않음

* **private**은 본인 클래스 내에서만 접근 가능
  [**Setter**](code.md) 와 [**Getter**](code.md)를 써서 내용 변경할 수 있음

**클래스**

* **public** 클래스는 다른 패키지의 클래스에서도 사용할 수 있음
* **default** 클래스는 같은 패키지에서만 사용 가능



#### abstract (추상)

* [**abstract**](code.md)로 지정된 메소드/클래스는 직접적으로 사용할 수 없음
  사용하기 위해서는 반드시 상속해서 사용해야 함



#### interface (인터페이스)

* 어떤 클래스가 있는데 특정한 [**인터페이스**](code.md)를 사용한다면, 그 클래스는 반드시 인터페이스의 메소드들을 구현해야한다

* 하나의 클래스가 여러개의 인터페이스를 구현할 수 있고, 상속도 가능
* 인터페이스 멤버는 반드시 public 이여야 한다

