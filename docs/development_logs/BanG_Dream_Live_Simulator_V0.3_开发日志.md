# 《BanG Dream! Live Simulator》开发学习日志

## 版本：V0.3
日期：2026-09-09  
状态：已完成 ✅

## 一、本版本目标

- 学习面向对象基础
- 使用 `class` 表示乐队、歌曲和角色
- 使用对象替代 V0.2 中的字典数据
- 学习对象属性、方法、`__init__` 和 `self`
- 学习 List 中保存对象
- 学习对象之间的组合关系
- 保留 V0.2 的 Live、输入检查、随机发挥、Score 和 Rank

## 二、本版本新增功能

- 新增 `Band` 类
- 新增 `Music` 类
- 新增 `Character` 类
- `bands` 改为保存 `Band` 对象
- `music` 改为保存 `Music` 对象
- `Band.members` 改为保存多个 `Character` 对象
- 新增 `Band.introduce()` 方法
- 新增 `Band.show_members()` 方法
- 将 `performance()` 拆分为 `performance_rate()` 和 `performance_condition()`
- 将 Live 进度显示封装为 `live()` 函数

## 三、本版本新学到的知识

### 1. Class 与 Object
`class` 用来定义一种对象的结构，对象是根据类创建出来的具体实例。

### 2. `__init__`
创建对象时初始化对象需要的数据。

### 3. `self`
表示当前正在操作的对象本身。

### 4. Attribute
对象保存的数据，例如 `Band.name`、`Band.power`、`Character.role`。

### 5. Method
属于对象自己的行为，例如 `Band.introduce()` 和 `Band.show_members()`。

### 6. List 保存对象
List 不只能保存字符串、数字和字典，也可以直接保存自定义对象。

### 7. 对象组合
`Band.members` 中保存多个 `Character` 对象，实现：
`Band → members → Character`。

### 8. 嵌套访问
可以从一个对象继续访问它内部保存的其他对象及其属性。

## 四、Bug / 问题记录

### Bug #01：不知道创建的对象应该放在哪里

**现象：** 创建多个 `Band` 和 `Music` 对象后，不知道如何统一调用和遍历。

**原因：** 一开始认为使用 Class 后就不再需要 List。

**解决：** 使用 List 统一保存多个同类对象。

**学到：** V0.2 的 List 没有被 OOP 替代，而是从 `List[Dict]` 变成了 `List[Object]`。

---

### Bug #02：不知道 Character 如何放进 Band

**现象：** 创建 `Character` 类后，不知道角色对象应该怎样与 Band 建立关系。

**解决思路：** `Band.members` 使用 List 保存多个 `Character` 对象。

**学到：** 一个对象可以保存其他对象，这属于对象组合。

---

### Bug #03：Character 属性命名错误

**现象：** `Character` 接收的是 `role`，但对象内部保存成了其他含义的属性名。

**原因：** `__init__` 参数名和实际 Attribute 没有保持一致。

**解决：** 重新检查参数与属性的对应关系。

**学到：** 构造参数和对象属性是两个不同概念，需要明确对应关系。

---

### Bug #04：Poppin'Party 成员数据重复

**现象：** 同一个成员被录入两次，不同职责对应了错误角色。

**原因：** 数据录入错误。

**学到：** 程序可以正常运行，但数据本身仍可能出错；需要区分语法错误、逻辑错误和数据错误。

## 五、本版本中的设计决定

### 设计决定 1：Character 不单独保存所属 Band

**决定：** 当前通过 `Band.members` 表示角色所属关系。

**原因：** 避免 Band 和 Character 之间出现重复的双向关系。

**未来：** 如果以后需要从 Character 反向找到 Band，再重新考虑。

### 设计决定 2：Character 直接创建在 Band.members 中

**决定：** 角色对象直接放入对应 Band 的成员列表。

**原因：** 当前主要通过 Band 管理角色，数据结构更直观。

### 设计决定 3：Music.affiliation 暂时保留字符串

**决定：** 歌曲所属乐队暂时保存为字符串。

**原因：** V0.3 重点是基础 OOP，对象引用留到后续版本处理。

## 六、仍然存在的问题

- `Music.affiliation` 仍是字符串，不是 `Band` 对象引用
- `rate` 仍是全局变量
- `index` 仍与 List 位置存在关联
- `Live` 目前仍是普通函数
- Score、Rank 仍由外部函数处理

## 七、我认为还可以优化的地方

- 后续将一场 Live 设计成独立对象
- 研究对象之间应该保存字符串还是对象引用
- 进一步明确不同类的职责
- 支持连续进行多场 Live

## 八、本版本测试情况

- Band 对象创建：通过
- Music 对象创建：通过
- Character 对象创建：通过
- List 保存对象：通过
- Band 内保存 Character 对象：通过
- 遍历 Band：通过
- 遍历 Band.members：通过
- `introduce()`：通过
- `show_members()`：通过
- 原 V0.2 Live 流程：通过

## 九、本版本最重要的收获

1. 真正理解了 `class`、对象、属性和方法的基本关系
2. 理解 List 仍然用于管理多个对象
3. 理解一个对象可以包含其他对象，形成对象组合关系

## 十、版本反思

### 与上一版本相比，我进步的地方

- 从 `List + Dict` 进入 `List + Object`
- 开始思考数据应该属于哪个对象
- 开始通过 Method 表示对象自己的行为
- 开始理解对象之间可以建立层级关系

### 我目前仍然比较薄弱的地方

- 对象之间应该如何建立引用
- 一个功能应该属于哪个类
- 多个对象之间如何协作

### 如果重新开发这一版

会更早先画出：
`bands → Band → members → Character`
这样的对象关系，再开始写代码。

## 十一、下一版本准备

### 下一版本计划进入

V0.4：对象关系与 Live 对象

### 预计需要学习的新知识

- 对象引用
- 对象之间的关系
- 对象职责划分
- `Live` 类设计
- 对象协作

### 我目前最担心的问题

- 不清楚 Live 应该保存哪些对象和状态
- 不清楚 Band、Music、Character、Live 之间谁应该引用谁
